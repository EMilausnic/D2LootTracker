
<template>
  <div>
      <!-- <button
      @click="getGun">
        get gun
      </button>

      <button 
        @click="queryThePlatform">
        query platform,
      </button>

      <button
      @click="getProfile">
        Get users profile
      </button>
      
      <button
      @click="haveUserSignInOnDiffTab">
        Link through a new tab
      </button>
      
      <button
      @click="getTokenResponce">
        gety users token
      </button> -->
      
      <button
      @click="fillGearList">
        get gear list filled
      </button>

      <button
      @click="makeAPITestCall">
        hello API?
      </button>

      <button
      @click="putItemInDatabase">
        add item into database
      </button>


      <table>
        <tr>
          <td>Item Name</td>
          <td>Source Location</td>
          <td>Hash for this item</td>
        </tr>
        <tr v-for="gear in gearList">
          <td>{{gear.name}}</td>
          <td>{{gear.sourceString}}</td>
          <td>{{gear.hash}}</td>
          <td>
            <img :src="gear.iconLink"/>
          </td>
        </tr>
      </table>
  </div>
</template>


<script>
  import data from "./simplified_file_shortned.json";

  export default {
  created() {
    this.handleCallback();
  },
  data() {
    return {
      gearDict: data,
      gearList: [],
    }
  },
  methods: {
    fillGearList() {
      Object.values(data).forEach(item => {
        // Adding this in to space things out a little better
        this.gearList.push({
          name: "======================",
          sourceString: "=============================",
          hash: "======================",
        })  

        this.gearList.push({
          name: item.displayProperties.name,
          iconLink: "https://www.bungie.net"+item.displayProperties.icon,
          sourceString: item.sourceString,
          hash: item.hash,
        })  
      });
      console.log(this.gearList)
    },
    makeAPITestCall() {
      // this works! I am able to get all items from the test ap that I made!
      let APITestURL = "https://con9zmebbb.execute-api.us-east-1.amazonaws.com/items";
      let xhr = new XMLHttpRequest();
      
      xhr.open("GET", APITestURL, true);
     
      xhr.onreadystatechange = function(){
        if(this.status === 200){
          console.log("this.responseText: "+this.responseText);
        }
        else{
          console.log("failed??")
        }
      }

      xhr.send(); 
    },
    putItemInDatabase() {
      let APITestURL = "https://con9zmebbb.execute-api.us-east-1.amazonaws.com/items";

      // Define the JSON object you want to send to the API
      const item = {
        ItemHash: 'test_item_from_website',
        Name: 'name_from_website',
        SourceString: 'source_string_from_website'
      }

      // Convert the JSON object to a string
      const itemJSON = JSON.stringify(item);
      console.log("stringified json object: " + itemJSON)
      let xhr = new XMLHttpRequest();
      
      xhr.open("PUT", APITestURL, true);
      // Set the Content-Type header to application/json
      xhr.setRequestHeader("Content-Type", "application/json");
      // xhr.setRequestHeader('Access-Control-Allow-Origin', 'http://localhost:5173');
     
      xhr.onreadystatechange = function(){
        if(this.status === 200){
          console.log("this.responseText: "+this.responseText);
        }
        else{
          console.log("failed??")
        }
      }

      xhr.send(itemJSON); 
    },
    queryThePlatform() {
      let apiKey = "14e8991258cb40dbb21198e66f69edbe";
      let client_id = "45889";
      let state = "6i0mkLx79Hp91nzWVeHrzHG4";
      let authURL = "https://www.bungie.net/en/OAuth/Authorize?client_id=45889&response_type=code&state="+state;
      let xhr = new XMLHttpRequest();
      xhr.open("GET", authURL, true);
      xhr.setRequestHeader("X-API-Key", apiKey);
      xhr.setRequestHeader('Access-Control-Allow-Origin', 'https://www.bungie.net');
      xhr.setRequestHeader("client_id", client_id);
      xhr.setRequestHeader("status", "6i0mkLx79Hp91nzWVeHrzHG4");


      xhr.onreadystatechange = function(){
      if(this.readyState === 4 && this.status === 200){
        let json = JSON.parse(this.responseText);
        console.log(json.Response);
        // console.log(json.Response.data.inventoryItem.itemName); //Gjallarhorn
      }
        else{
          console.log("failed??")
        }
      }
      xhr.send();
    },
    getGun() {
      let apiKey = "14e8991258cb40dbb21198e66f69edbe";

      let xhr = new XMLHttpRequest();
      xhr.open("GET", "https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/1274330687/", true);
      xhr.setRequestHeader("X-API-Key", apiKey);
        // this shit makes it not work
      // xhr.setRequestHeader('Access-Control-Allow-Origin', '*'); // bad
      // xhr.setRequestHeader("Access-Control-Allow-Headers", "*"); // bad
      // xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded"); // good
      // xhr.setRequestHeader("Access-Control-Allow-Methods", "*"); // bad
      // end of shit that dont work

      xhr.onreadystatechange = function(){
      if(this.readyState === 4 && this.status === 200){
        let json = JSON.parse(this.responseText);
        console.log(json); //Gjallarhorn
        console.log(json.Response.data.inventoryItem.itemName); //Gjallarhorn
      }
      } 

      xhr.send();
    },
    getProfile() {
      // have user sign in 
      let apiKey = "14e8991258cb40dbb21198e66f69edbe";
      let client_id = "45889";
      let auth_code_holder = "";

      let xhr = new XMLHttpRequest();
      xhr.open("GET", "https://www.bungie.net/en/OAuth/Authorize?client_id={"+client_id+"}&response_type=code/", true);
      xhr.setRequestHeader("X-API-Key", apiKey);
      // xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
      // xhr.setRequestHeader("Access-Control-Allow-Headers", "*");
      // xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded");
      // xhr.setRequestHeader("Access-Control-Allow-Methods", "*");
    

      xhr.onreadystatechange = function(){
        if(this.readyState === 4 && this.status === 200){
          let json = JSON.parse(this.responseText);
          auth_code_holder = JSON.parse(this.responseText);
          console.log(json); 
          console.log(auth_code_holder); 
        }
      }

      xhr.send();

      // get token response
      let xhr2 = new XMLHttpRequest();
      xhr2.open("POST", "https://www.bungie.net/Platform/App/OAuth/Token/", true);
      xhr2.setRequestHeader('client_id', client_id); 
      // xhr2.setRequestHeader('Content-Type', application/x-www-form-urlencoded);
      xhr2.setRequestHeader('grant_type', "authorization_code");
      xhr2.setRequestHeader('code', "9c4d4bfb54e6939177765ddea62cafb8");
      // xhr2.setRequestHeader("X-API-Key", apiKey);
      // xhr2.setRequestHeader('Access-Control-Allow-Origin', '*');
  

      xhr2.onreadystatechange = function(){
      if(this.readyState === 4 && this.status === 200){
        let json = JSON.parse(this.responseText);
        console.log(json); 
      }
      }

      xhr2.send();
  },
    haveUserSignInOnDiffTab() { 
      // ok so this is kindaa working? 
      // current issues: the Authorization query string parameters are not valid.
        let client_id = "45889";
      // "https://www.bungie.net/en/OAuth/Authorize?client_id={"+client_id
      let authorizeUrl = "https://www.bungie.net/en/OAuth/Authorize?client_id=45889&response_type=code";
      // let authorizeUrl = "https://www.bungie.net/en/OAuth/Authorize";

      // App Window
      localStorage.setItem('tabbed', true);
      window.open(authorizeUrl);
      window.addEventListener('storage', function(e) {
          if(localStorage.getItem('tabbed') && localStorage.getItem('tabbed')) {
              // Reload authorization code from LocalStorage
              localStorage.removeItem('tabbed');
          }
      });

      // Authorize/Redirect Window
      if (localStorage.getItem('tabbed')) {
          // Save authorization code to LocalStorage and close the tab
          // let auth_code = "41e7e05bb854277edbd71ecb10536695";
          // console.log("auth code = "+localStorage.authorization_code);
          window.close();
      }

      
      console.log('attmetping to get code responcse');
      console.log('responce from:', this.$route.query.code);
      let code = this.$route.query.code;
      console.log('Code from URL:', code);


      // // get token response
      // let xhr2 = new XMLHttpRequest();
      // xhr2.open("POST", "https://www.bungie.net/Platform/App/OAuth/Token/", true);
      // xhr2.setRequestHeader('client_id', client_id); 
      // // xhr2.setRequestHeader('Content-Type', application/x-www-form-urlencoded);
      // xhr2.setRequestHeader('grant_type', "authorization_code");
      // xhr2.setRequestHeader('code', "9940e0eb1214b57e108fb24574776c4e");
      // // xhr2.setRequestHeader("X-API-Key", apiKey);
      // // xhr2.setRequestHeader('Access-Control-Allow-Origin', '*');


      // xhr2.onreadystatechange = function(){
      //   if(this.readyState === 4 && this.status === 200){
      //     let json = JSON.parse(this.responseText);
      //     console.log(json); 
      //   }
      // }

      // xhr2.send();
    },
    getTokenResponce() {
      // let client_id = "45889";
      // get token response
      let xhr2 = new XMLHttpRequest();
      xhr2.open("POST", "https://www.bungie.net/Platform/App/OAuth/Token/?grant_type=authorization_code&code=41e7e05bb854277edbd71ecb10536695", true);
      // xhr2.open("POST", "https://www.bungie.net/Platform/App/OAuth/Token/", true);
      // xhr2.setRequestHeader('client_id', client_id); 
      xhr2.setRequestHeader('Content-Type', application/x-www-form-urlencoded);
      xhr2.setRequestHeader('grant_type', "authorization_code");
      xhr2.setRequestHeader('code', "41e7e05bb854277edbd71ecb10536695");
  
      xhr2.onreadystatechange = function(){
        if(this.readyState === 4 && this.status === 200){
          let json = JSON.parse(this.responseText);
          console.log(json); 
        }
      }

      xhr2.send();
    },
    handleCallback() {
      const urlParams = new URLSearchParams(window.location.search);
      const code = urlParams.get('code');

      if (code) {
        // Perform authentication logic with the received code
        console.log('Code from URL:', code);
      }
    },
  },
};
</script>

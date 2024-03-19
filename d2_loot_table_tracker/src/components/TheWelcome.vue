
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

      <v-btn
      @click="makeAPITestCall">
      get items from API
      </v-btn>

      <v-btn
      @click="AddSOMEItemsFromAPI">
      Log a few items form api, must make api call first
      </v-btn>

      <v-btn
      @click="getSourceStringItems">
      get all Solcstise items
      </v-btn>


      <v-btn
      @click="getItemsUsingSourceStringList">
      get items forn database using the given source 
      </v-btn>

      <v-btn
      @click="putItemInDatabase">
        add single item into database
      </v-btn>

      <!-- <p>Enter testerItemName: {{ testerItemName }}</p> -->
      <v-text-field 
        v-model="testerItemName" 
        label="Enter item name"
       />

      <!-- <p>Enter testerItemHash: {{ testerItemHash}}</p> -->
      <v-text-field v-model="testerItemHash"
        label="Enter item hash" />

      <!-- <p>Enter testerItemSource: {{ testerItemSource }}</p> -->
      <v-text-field v-model="testerItemSource" 
        label="Enter item source" />



      <v-btn
      @click="putMultiupleItemsInDatabase">
        add 2 test items into the database
      </v-btn>

      <v-btn
      @click="ParseItemsToPush">
        put everything into the database!
      </v-btn>

      <v-item-group>
        <v-item v-for="(itemsFromSource, sourceString) in ItemsFromDatabase" style="margin-bottom: 5px;">
            {{ sourceString }}
          <div class="align-center" style="margin: 5px;">
            <!-- <div> -->
            <v-card 
            v-for="(item, index) in itemsFromSource"  
            :key="index"
            style="margin: 5px;"
            >
              <!-- {{ item }} -->
              <template v-slot:prepend>
                <img v-if="item.iconLink && item.iconLink['S']" :src="'https://www.bungie.net' + item.iconLink['S']" width="96px" height="96px"/> 
              </template>

              <!-- <template v-slot:prepend>
                <img :src="item.iconLink" width="96px" height="96px"/> 
              </template> -->
                <v-card-text class="text-h5 py-2">
                  <!-- TODO: figure out why I need to include ["S"] on all of these -->
                  {{item.Name["S"]}}
                </v-card-text>

                <v-card-text class="py-1">
                  Gear Hash: {{item.ItemHash["S"]}}
                </v-card-text>

                <!-- <v-card-text class="py-0" >
                  {{item.SourceString["S"]}}
                </v-card-text> -->

                <v-card-text class="py-0" >
                  {{item.itemTypeAndTierDisplayName["S"]}}
                </v-card-text> 

               <v-card-text class="py-0" >
                  {{item.itemTypeDisplayName["S"]}}
                </v-card-text>
              </v-card>
              

          </div>
        </v-item>
      </v-item-group>
  </div>
</template>


<script>
  import items from "./FullDatabaseFIle.json";
  import { VueElement } from "vue";
import data from "./modified_file_truncated.json";
  import data2 from "./testingSendManyItemsToDatabase.json";

  export default {
  created() {
    this.handleCallback();
    // TODO: call the function that gets all of the items from the database (from like 2 sources for now)
  },
  data() {
    return {
      testerItemSource: "",
      testerItemHash: "",
      testerItemName: "",
      responceData: [],
      ItemsFromDatabase:{},
      listOfSourceStrings: ["Solstice", "Xûr", "Last Wish raid.", "Bright Engrams"]
    }
  },
  methods: {
    // fillGearList() {
    //   Object.values(data).forEach(item => {

    //     this.gearList.push({
    //       name: item.displayProperties.name,
    //       iconLink: "https://www.bungie.net"+item.displayProperties.icon,
    //       sourceString: item.sourceString,
    //       hash: item.hash,
    //     })  
    //   });
    //   // only pick a few items to show
      
    //   console.log(this.gearList)
    // },
    getSourceStringItems() {
      let sourceString = "Solstice"
      let APITestURL = "https://con9zmebbb.execute-api.us-east-1.amazonaws.com/" +sourceString;
      let xhr = new XMLHttpRequest();
      
      xhr.open("GET", APITestURL, true);
     
      xhr.onreadystatechange = function(){
        if(this.status === 200){
          let response = JSON.parse(this.responseText);
          let items = response.Items; // Accessing the "Items" property
          console.log("Items:", items);
          this.ItemsFromDatabase = { ...this.ItemsFromDatabase, [sourceString]: items }; // ok cool not 100% sure why this works and I should look into it more but it does!
          console.log(this.ItemsFromDatabase)
          //  loop through the items array and access individual items
      //     items.forEach(item => {
      //       console.log("Name:", item.Name.S);
      //       // Access other properties as needed
      // });
        }
        else{
          console.log("failed?? on"+sourceString)
        }
      }

      xhr.send(); 
    },
    getItemsUsingSourceStringList() {
      const promises = [];

    for (let i = 0; i < this.listOfSourceStrings.length; i++) {
        const sourceString = this.listOfSourceStrings[i];
        let APITestURL = "https://con9zmebbb.execute-api.us-east-1.amazonaws.com/" + sourceString;

        // Create a promise for each API call
        const promise = new Promise((resolve, reject) => {
            let xhr = new XMLHttpRequest();
            xhr.open("GET", APITestURL, true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        const response = JSON.parse(xhr.responseText);
                        resolve({ sourceString, items: response.Items });
                    } else {
                        reject(`Failed to fetch items for ${sourceString}`);
                    }
                }
            };
            xhr.send();
        });

        promises.push(promise);
    }

    // Wait for all promises to resolve
    Promise.all(promises)
        .then(results => {
            // Populate ItemsFromDatabase dictionary
            results.forEach(({ sourceString, items }) => {
                this.ItemsFromDatabase[sourceString] = items;
            });
            console.log("ItemsFromDatabase:", this.ItemsFromDatabase);
        })
        .catch(error => {
            console.error(error);
        });
    },
    //   // Object.values(this.listOfSourceStrings).forEach(sourceString => {
    //   for (let i = 0; i < this.listOfSourceStrings.length; i++) {
    //     const sourceString = this.listOfSourceStrings[i];
    //     let APITestURL = "https://con9zmebbb.execute-api.us-east-1.amazonaws.com/" +sourceString;
    //     let xhr = new XMLHttpRequest();
    //     let items = [];
    //     xhr.open("GET", APITestURL, true);
      
    //     xhr.onreadystatechange = function(){
    //       if(this.status === 200){
    //         let response = JSON.parse(this.responseText);
    //         items = response.Items; // Accessing the "Items" property
    //         console.log("Items:", items);
    //         // ok cool not 100% sure why this works and I should look into it more but it does!
    //         // this.ItemsFromDatabase = { ...this.ItemsFromDatabase, [sourceString]: items }; 
    //         // console.log(this.ItemsFromDatabase)
    //       }
    //       else{
    //         console.log("failed?? on"+sourceString)
    //       }
    //     }
 
    //     xhr.send(); 
    //     // for the items to be correctly added to the dictionary they have to be added here and not in the onreadystatechange part
    //     this.ItemsFromDatabase[sourceString] = items;
    //   }
    //   // })
    //   console.log("after getting all the items")
    //   console.log(this.ItemsFromDatabase)
    // },
    makeAPITestCall() {
      // this works! I am able to get all items from the test ap that I made!
      let APITestURL = "https://con9zmebbb.execute-api.us-east-1.amazonaws.com/items";
      let xhr = new XMLHttpRequest();
      // let responceData = "";
      xhr.open("GET", APITestURL, true);
     
      console.log(typeof this.responceData);
      xhr.onreadystatechange = function(){
        if(this.status === 200){
          // console.log("this.responseText: "+this.responseText);
          this.responceData = this.responseText // ISSUE this is a string and make sthings supperrrrr annnoyyying
          console.log("responceData "+this.responceData);
          console.log("responceData "+this.responceData.length);
      console.log(typeof this.responceData);
          
        }
        else{
          console.log("failed??")
        }
      }

      xhr.send(); 
    },
    AddSOMEItemsFromAPI() {


    },
    GetItemsFromDatabase() {
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

      // // Define the JSON object you want to send to the API
      // const item = {
      //   itemHash: 'test_item_from_website',
      //   name: 'name_from_website',
      //   sourceString: 'source_string_from_website'
      // }

      // Define the JSON object using text boxes
      const item = {
        itemHash: this.testerItemHash,
        name: this.testerItemName,
        sourceString: this.testerItemSource
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
    putMultiupleItemsInDatabase() {
      let APITestURL = "https://con9zmebbb.execute-api.us-east-1.amazonaws.com/manyitems";

      // Define the JSON object you want to send to the API
      name_data = {
        name: "test_name"
      }
      const item3 = {
          itemHash: 'test_item_from_website3',
          displayProperties: name_data,
          sourceString: 'source_string_from_website3',
          itemTypeDisplayName: 'itemTypeDisplayName3',
          itemTypeAndTierDisplayName: 'itemTypeAndTierDisplayName3',
      }
      const item2 = {
          itemHash: 'test_item_from_website2',
          displayProperties: name_data,
          sourceString: 'source_string_from_website2',
          itemTypeDisplayName: 'itemTypeDisplayName2',
          itemTypeAndTierDisplayName: 'itemTypeAndTierDisplayName2',
      }
      const items = [item2, item3]
      // Now create the request object including the items array
      const requestObject = {
          items: items
      }
      // Convert the JSON object to a string
      const itemJSON = JSON.stringify(requestObject);
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
    ParseItemsToPush() { 
      let APITestURL = "https://con9zmebbb.execute-api.us-east-1.amazonaws.com/manyitems";
      let itemsArray = Object.values(items)
      // let itemsArray = Object.values(data2)
      // Split the itemsArray into chunks of 50 items each
      const chunkSize = 25;
      for (let i = 0; i < itemsArray.length; i += chunkSize) {
          // setTimeout(() => {}, 100000);
          const chunk = itemsArray.slice(i, i + chunkSize);

          const requestObject = {
              items: chunk
          };

          // Convert the JSON object to a string
          const itemJSON = JSON.stringify(requestObject);
          console.log("Sending chunk:", chunk);

          let xhr = new XMLHttpRequest();
          xhr.open("PUT", APITestURL, true);
          // Set the Content-Type header to application/json
          xhr.setRequestHeader("Content-Type", "application/json");

          xhr.onreadystatechange = function() {
              if (this.readyState === 4) {
                  if (this.status === 200) {
                      console.log("Chunk sent successfully:", chunk);
                      console.log("Response:", this.responseText);
                  } else {
                      console.error("Failed to send chunk:", chunk);
                      console.error("Response:", this.responseText);
                  }
              }
          };

          xhr.send(itemJSON);
        }
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

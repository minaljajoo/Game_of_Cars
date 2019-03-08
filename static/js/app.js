/*   Project 3: imdb-dashboard 
JavaScript file: Purpose- initializations of index.html with carousel and default settings 
Also take user input and update the index.html   */
/*************** Set all the variables ***********/

// allShows must be passed in from flask -> index.html 



/*************** Initialize the dashboard ***********/
function init() {

  let models = allModels.model;
  let ids = allModels.id;
  console.log(models)
  console.log(ids)
  }
  //-----------------------------------------
  //Plot all the plots with the default shows 
  
/**************************

//------------------------------------
// Function:add_element_to_array
// Add the shows to 'listSerials' array 
function add_element_to_array() {
  //Check for the  max. show entries count
  if (seriesCount == maxSeries) {
    alert("You have entered max no of series");
    document.getElementById("myInput").value = "";
  } else {
    // Check if user enter any show name
    var inputSeries = document.getElementById("myInput").value;
    if (inputSeries == "" || inputSeries == null) {
      alert("You haven't entered anything");
    } else {
      //Call a function to check if the user entered  new show name from the list
      if (searchNewSeries(inputSeries)) {
        //Call a function to check if it is valid show name from the list
        if (searchSeries(inputSeries)) {
          // If it is valid new show entry then add it to the array 'listSerials' 
          listSerials[x] = inputSeries;
          document.getElementById("myInput").value = "";
          update_array(listSerials[x]);
          seriesCount++;
          x++;
        }
      } else {
        document.getElementById("myInput").value = "";
      }
    }
  }
}
//------------------------------------
//Function: searchNewSeries
//Check if the user entered  new show name from the list
function searchNewSeries(newSeries) {
  var flag = true;
  for (var i = 0; i < listSerials.length; i++) {
    if (newSeries === listSerials[i]) {
      flag = false;
    }

  }
  if (flag == false) {
    alert("The show was already selected");
  }
  return flag;
}
//------------------------------------
//Function: searchSeries
//Check if it is valid show name from the list
function searchSeries(enterSeries) {
  var flag = false;
  for (var i = 0; i < series.length; i++) {
    if (enterSeries === series[i]) {
      flag = true;
    }

  }
  if (flag == false) {
    alert("No such show was found");
  }
  return flag;
}
//------------------------------------
//Function: update_array
//Display the show entered by user to the 'Update Plot' card
function update_array(newSeries) {
  var li = document.createElement('li');
  var ul = document.getElementById('seriesList');
  var xButton = document.createElement("button");
  var seriesName = newSeries + " ";
  li.setAttribute('id', x);
  li.appendChild(document.createTextNode(seriesName));
  ul.appendChild(li);
  xButton.setAttribute('id', x);
  xButton.setAttribute("onclick", "removeSeries(" + x + ")");
  xButton.setAttribute("class", "sourceText fas fa-times");
  $(xButton.sourceText).append('<i class="fas fa-times"></i>');
  li.appendChild(xButton);
}

//------------------------------------
//Function: removeSeries
//Remove the show name from list if user click on 'x' button
function removeSeries(itemid) {
  var item = document.getElementById(itemid);
  var ul = document.getElementById('seriesList');
  ul.removeChild(item);
  delete listSerials[itemid];
  var checkArray = listSerials.every(function (v) {
    return v === null;
  });

  if (checkArray) {
    resetAll();
  } else {
    seriesCount--;
  }
}
//------------------------------------
//Function: resetAll
//Reset all the variables and list element 
function resetAll() {
  document.getElementById("seriesList").innerHTML = "";
  x = 0;
  seriesCount = 0;
  listSerials = [];
}
/*************** Initialize the dashboard ***********/
init();

/************************ End of app.js JavaScript file ************************ */
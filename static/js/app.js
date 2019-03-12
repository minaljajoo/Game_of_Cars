/*   Final Project: Game of Cars-dashboard
JavaScript file: Purpose- initializations of prediction.html 
  */
/*************** Set all the variables ***********/

// allShows must be passed in from flask -> index.html 



/*************** Initialize the dashboard ***********/
function init() {

  var sactual = valModels.smartwayTest;
  var mactual = valModels.mpgTest;
  var vmodels = valModels.TestModels;
  var spred = valModels.smartwayPred;
  var mpred = valModels.mpgPred;
  console.log(vmodels);
  console.log(spred);
  console.log(mpred);





}
//-----------------------------------------
//
function update_model(mod_name) {
  var mpg_str = ''
  var smart_str = ''
  var sactual = valModels.smartwayTest;
  var mactual = valModels.mpgTest;
  var vmodels = valModels.TestModels;
  var spred = valModels.smartwayPred;
  var mpred = valModels.mpgPred;
  console.log("update model")
  for (var i = 0; i < 8; i++) {
    if (vmodels[i] == mod_name) {
      if (mpred[i] == 2) {
        mpg_str = 'High MPG i.e. MPG more than 50mpg';
      } else if (mpred[i] == 0) {
        mpg_str = 'Low MPG i.e. MPG less than 23mpg';
      } else if (mpred[i] == 1) {
        mpg_str = 'Medium MPG i.e. MPG in range of 23mpg to 50mpg';
      };

      if (spred[i] == 0) {
        smart_str = 'This vehical is a ELITE Smartway vehicle';
      } else if (spred[i] == 1) {
        smart_str = 'This vehical is not a Smartway vehicle';
      } else if (spred[i] == 2) {
        smart_str = 'This vehical is a Smartway vehicle';
      };
      ampg_str = ('Actual: MPG value is ' + mactual[i]);
      asmart_str = ('Actual: Smartway value is ' + sactual[i]);
      document.getElementById('predModel').innerHTML = mod_name;
      document.getElementById('actualMpg').innerHTML = ampg_str;
      document.getElementById('actualSmart').innerHTML = asmart_str;
      document.getElementById('predMpg').innerHTML = mpg_str;
      document.getElementById('predSmart').innerHTML = smart_str;

    }

  }


}
/*************** Initialize the dashboard ***********/
console.log("start js");
init();

/************************ End of app.js JavaScript file ************************ */
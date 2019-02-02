function parseCSV(file, callback){ 
    var parsedData;
    Papa.parse(file, {
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            parsedData = results.data;
            callback(parsedData);
            createGrid(parsedData);
        }
    });
}

function displayData(CSVdata){
    console.log("Data: ", CSVdata)
}

function handleFileSelect(evt) {
    var file = evt.target.files[0];
    parseCSV(file,displayData);
}

$(document).ready(function(){
    $("#csv-file").change(handleFileSelect);
});
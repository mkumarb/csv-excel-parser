function createGrid(csvData){
    var data = csvData;
    // Sample Data
    // [
    //     { symbol: 'APPL', name: 'Apple Inc.', prevclose: 93.13 },
    //     { symbol: 'MSFT', name: 'Microsoft Corporation', prevclose: 51.91 },
    //     { symbol: 'TSLA', name: 'Tesla Motors Inc.', prevclose: 196.40 },
    //     { symbol: 'IBM', name: 'International Business Machines Corp', prevclose: 155.35 }
    // ];
    var gridOptions = {
        canvasContextAttributes: { alpha: true },
        margin: {left: '20px' } 
    };
    var grid = new fin.Hypergrid(gridOptions);
    grid.setData(data);
    var fields = ["SYM","NAME","CLOSE"];
    // grid.setFields(fields);
    grid.addProperties({
        showRowNumbers: true,
        editable: true,
        editor: "Textfield",
        checkboxOnlyRowSelections: false,
        autoSelectRows: false
    });
}
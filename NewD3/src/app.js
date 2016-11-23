document.body.innerHTML = `<h1>${d3.version}</h1>`;

var linearScale = d3.scaleLinear().domain([0,100]).range([0,600]).clamp(true);
var timeScale = d3.scaleTime().domain([new Date(2016, 0, 1), new Date()]).range([0,100]);

d3.csv('data/data.csv', function(data) {
    console.log(data);
});
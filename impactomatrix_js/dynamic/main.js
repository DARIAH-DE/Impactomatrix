$.getJSON('impactomatrix.json', function(impact_data) {
    var impact_area = 20;

    // producing the list for factors
    var factors_output="<ul>" ;
    for (var i in impact_data.impacts[impact_area].has_factors) {
        var key = impact_data.impacts[impact_area].has_factors[i]
        // this loop is somewhat over the top
        for (var j in impact_data.factors) {
            if (impact_data.factors[j].slug == key)
                var factors_name = impact_data.factors[j].name
        }
        factors_output+="<li>" + factors_name + "</li>"
    };
    factors_output+="</ul>";

    // producing the list for criteria, same code as above
    var criteria_output="<ul>";
    for (var i in impact_data.impacts[impact_area].has_criteria) {
        var key = impact_data.impacts[impact_area].has_criteria[i]
        for (var j in impact_data.criteria) {
            if (impact_data.criteria[j].slug == key)
                var criteria_name = impact_data.criteria[j].name
        }
        criteria_output+="<li>" + criteria_name + "</li>"
    };
    criteria_output+="</ul>";

    var output="<strong>" + impact_data.impacts[impact_area].name + "</strong><br/>" + impact_data.impacts[impact_area].description;
    
document.getElementById("factors").innerHTML=factors_output;
document.getElementById("criteria").innerHTML=criteria_output;
document.getElementById("area").innerHTML=output;
});





var influCount = influencerCount


console.log(interestCount[4][1])
console.log(influCount)

$(function () {
    (function (H) {
    //DATALABELS
            H.wrap(H.Series.prototype, 'drawDataLabels', function (proceed) {
                var css = this.chart.options.drilldown.activeDataLabelStyle;
                proceed.call(this);

                css.textDecoration = 'none';
                css.fontWeight = 'normal';
                css.cursor = 'default';
                css.color = 'black';

                H.each(this.points, function (point) {

                    if (point.dataLabel) { // <-- remove 'point.drilldown &&' 
                        point.dataLabel
                            .css(css)
                            .on('click', function () {
                                return false;
                            });
                    }
                });
            });
        })(Highcharts);


    Highcharts.setOptions({
        lang: {

            drillUpText: '<< Back'
        },
    });
    $('#container').highcharts({
        chart: {
            type: 'bar',
            zoomType: 'y',
            events: {

                drilldown: function(e) {
                    if(e.point.y == null) {
                        e.point.update({
                            y:oldy
                        })
                    }  

                    /*
                    var $button = $('#button');
                    $button.click(function() {
                        console.log($('#container').highcharts())
                        var name  = "Casual Users"
                        console.log(e.seriesOptions.name);
                        if (this.name == "Casual Users" && this.visible == true) {
                            this.visible = false;
                            $button.html('Show Casual Users');
                        }else{
                            this.visible == true;
                            $button.html('Hide Casual Users');
                        }
                    });
                    console.log(e.seriesOptions.data[0][1])
                    e.seriesOptions.data[0][1] = 0
                    
                    */
                    
                    drawDistChart(e.seriesOptions.name);
                    
                },
                drillup: function(e) {
                    drawDistChart(null);
                }
            }
        },
        tooltip: {
            formatter: function() {
                if (this.point.drilldown == undefined)
                    return this.y + " followers are " + this.key;
                else
                    return this.y + " followers are interested in " + this.point.drilldown ;
            }
        },
        title: {
            text: 'Follower Interests'
        },
        subtitle: {
            text: 'Select a bar to view amount of Influencers within an Interest || Click & Drag to zoom'
        },
        xAxis: {
           type: 'category',
           gridLineWidth:0,
           minorGridLineWidth: 0
           //categories: ['Tech', 'Sports','Art','Food','Politics','Business','Unknown', 'Gaming','Fashion','Music'] 
                    },
        yAxis: {
            minorGridLineWidth: 0,
            gridLineWidth:0,
            minPadding: 30,
            min: 0,
            title: {
                text: 'Amount of Followers'
            }
        },
        legend: {
            enabled: true,
            reversed: true
            
        }
,        credits: {
            enabled: false
        },
        plotOptions: {
            series: {
                stacking: 'percent',
                borderWidth: 1,
                dataLabels: {
                    formatter: function() {
                        if(this.y > 0) {
                            var pct = (this.y/total)*100;
                            //console.log(this)
                            //console.log(this.point.name)
                            //console.log(this.point.visible)
                            if (this.point.drilldown == undefined)
                                return this.y;
                            else
                                return Math.round(pct) + '%';
                        }
                    },
                    enabled: true,
                    style: {
                        color: "black",
                        textShadow: false,
                        textDecoration: "none"
                    }
                }
                
               /* point: {
                    events : {
                        click: function(e) {
                            console.log(drilldown[e])
                            drawDistChart(this.name);
                        }
                        {
                        drilldown: function(e) {
                            console.log(e)
                        }
                    }
                }*/
            }
        },
        series: [  
            {
            name : 'Unknown', 
            data : [{
                name: 'Unknown',
                y: interestUnknown[0][0],
                drilldown: 'Unknown'
            }],
            visible: false
            }, {
            name : interestCount[0][1],    
            data : [{
                name: interestCount[0][1],
                y: interestCount[0][0],
                drilldown: interestCount[0][1]
            }]}, {
            name : interestCount[1][1],    
            data : [{
                name: interestCount[1][1],
                y: interestCount[1][0],
                drilldown: interestCount[1][1]
            }]},
            {
            name : interestCount[2][1],
            data : [{
                name: interestCount[2][1],
                y: interestCount[2][0],
                drilldown: interestCount[2][1]
            }]}, {
            name : interestCount[3][1],
            data : [{
                name: interestCount[3][1],
                y: interestCount[3][0],
                drilldown: interestCount[3][1]
            }]}, {
            name : interestCount[4][1],
            data : [{
                name: interestCount[4][1],
                y: interestCount[4][0],
                drilldown: interestCount[4][1]
            }]}, {
            name : interestCount[5][1],
            data : [{
                name: interestCount[5][1],
                y: interestCount[5][0],
                drilldown: interestCount[5][1]
            }]}, {
            name : interestCount[6][1],
            data : [{
                name: interestCount[6][1],
                y: interestCount[6][0],
                drilldown: interestCount[6][1]
            }]},  {
            name : interestCount[7][1],
            data : [{
                name: interestCount[7][1],
                y: interestCount[7][0],
                drilldown: interestCount[7][1]
            }]}, {
            name : interestCount[8][1],
            data : [{
                name: 'Influence',
                y: interestCount[8][0],
                drilldown: interestCount[8][1],
                /*tooltip: {
                    formatter: function() {
                        return interestCount[8][1]+ ' : ' + this.y; 
                    }
                }*/
            }]}
            ],
        drilldown: {
            
            drillUpButton: {
                relativeTo: 'spacingBox',
                position: {
                    y: 0,
                    x: 0
                },
                theme: {
                    fill: 'white',
                    'stroke-width': 1,
                    stroke: 'silver',
                    r: 0,
                    states: {
                        hover: {
                            fill: '#bada55'
                        },
                        select: {
                            stroke: '#039',
                            fill: '#bada55'
                        }
                    }
                }

            },

            series: [{/*
                events: {
                    click: function(e) {
                        console.log(this)
                        console.log(e.point)
                        //console.log(e.point.series.visible)
                      
                        if (e.point.y != null) {
                            var oldy = e.point.y
                            e.point.visible =;
                        }
                    }
                },*/
                name: 'Technology & Science',
                id: 'Technology & Science',
                data: [
                    ['Casual Users',influCount[0][0]],
                    ['Youtubers',influCount[1][0]],
                    ['Writer or Journalist',influCount[2][0]],
                    ['Celebrity',influCount[3][0]],
                    ['Business Expert',(influCount[4][0])],
                    ['Brand or Corporation',(influCount[5][0])],
                    ['Academic',(influCount[6][0])]
                ],
                stacking: 'normal'
            },{
                
                name: 'Fashion & Beauty',
                id: 'Fashion & Beauty',
                data: [
                    ['Casual Users',influCount[0][1]],
                    ['Youtubers',influCount[1][1]],
                    ['Writer or Journalist',influCount[2][1]],
                    ['Celebrity',influCount[3][1]],
                    ['Business Expert',influCount[4][1]],
                    ['Brand or Corporation',influCount[5][1]],
                    ['Academic',(influCount[6][1])]
                ],
                stacking: 'normal'

            },{
                
                name: 'Arts & Culture',
                id: 'Arts & Culture',
                data: [
                    ['Casual Users',influCount[0][2]],
                    ['Youtubers',influCount[1][2]],
                    ['Writer or Journalist',influCount[2][2]],
                    ['Celebrity',influCount[3][2]],
                    ['Business Expert',influCount[4][2]],
                    ['Brand or Corporation',influCount[5][2]],
                    ['Academic',(influCount[6][2])]
                ],
                stacking: 'normal'

            },{
                
                name : 'Sports & Fitness',
                id: 'Sports & Fitness',
                data: [
                    ['Casual Users',influCount[0][3]],
                    ['Youtubers',influCount[1][3]],
                    ['Writer or Journalist',influCount[2][3]],
                    ['Celebrity',influCount[3][3]],
                    ['Business Expert',influCount[4][3]],
                    ['Brand or Corporation',influCount[5][3]],
                    ['Academic',(influCount[6][3])]
                ],
                stacking: 'normal'

            },{
               
                name : 'Food & Drink',
                id: 'Food & Drink',
                data: [
                    ['Casual Users',influCount[0][4]],
                    ['Youtubers',influCount[1][4]],
                    ['Writer or Journalist',influCount[2][4]],
                    ['Celebrity',influCount[3][4]],
                    ['Business Expert',influCount[4][4]],
                    ['Brand or Corporation',influCount[5][4]],
                    ['Academic',(influCount[6][4])]
                ],
                stacking: 'normal'

            },{
                
                name: 'News & Politics',
                id: 'News & Politics',
                data: [
                    ['Casual Users',influCount[0][5]],
                    ['Youtubers',influCount[1][5]],
                    ['Writer or Journalist',influCount[2][5]],
                    ['Celebrity',influCount[3][5]],
                    ['Business Expert',influCount[4][5]],
                    ['Brand or Corporation',influCount[5][5]],
                    ['Academic',(influCount[6][5])]
                ],
                stacking: 'normal'

            },{
                
                name : 'Business & Finance',
                id: 'Business & Finance',
                data: [
                    ['Casual Users',influCount[0][6]],
                    ['Youtubers',influCount[1][6]],
                    ['Writer or Journalist',influCount[2][6]],
                    ['Celebrity',influCount[3][6]],
                    ['Business Expert',influCount[4][6]],
                    ['Brand or Corporation',influCount[5][6]],
                    ['Academic',(influCount[6][6])]
                ],
                stacking: 'normal'
            },{
                
                name: 'Gaming',
                id: 'Gaming',
                data: [
                    ['Casual Users',influCount[0][7]],
                    ['Youtubers',influCount[1][7]],
                    ['Writer or Journalist',influCount[2][7]],
                    ['Celebrity',influCount[3][7]],
                    ['Business Expert',influCount[4][7]],
                    ['Brand or Corporation',influCount[5][7]],
                    ['Academic',(influCount[6][7])]
                ],
                stacking: 'normal'

            },{
                
                name: 'Music',
                id: 'Music',
                data: [
                    ['Casual Users',influCount[0][8]],
                    ['Youtubers',influCount[1][8]],
                    ['Writer or Journalist',influCount[2][8]],
                    ['Celebrity',influCount[3][8]],
                    ['Business Expert',influCount[4][8]],
                    ['Brand or Corporation',influCount[5][8]],
                    ['Academic',(influCount[6][8])]
                ],
                stacking: 'normal'
            },{

                name: 'Unknown',
                id: 'Unknown',
                data: [
                    ['Casual Users',influCount[0][9]],
                    ['Youtubers',influCount[1][9]],
                    ['Writer or Journalist',influCount[2][9]],
                    ['Celebrity',influCount[3][9]],
                    ['Business Expert',influCount[4][9]],
                    ['Brand or Corporation',influCount[5][9]],
                    ['Academic',(influCount[6][9])]
                ],
                stacking: 'normal'
            }]
        }

    });


    /////////////////////////////////////////

/*
    var plotLeft = Highcharts.charts[0].plotLeft;
    var plotTop = Highcharts.charts[0].plotTop;
    $.each(Highcharts.charts[0].series,function(i, s){
        $.each(s.points, function(j, p){
            console.log('Series: ' + i +', Point: ' + j + ', Left: ' + (p.plotX ) +  ', Top: ' + (p.plotY ));
        });
    });
*/
});




function drawDistChart(category) {

    var distSeries = fulldistcount;
    var text = 'Distribution of Follower Influence Interested in ' + category;
    
    if (category == 'Technology & Science') {
        var distSeries = techdistcount;
        var distuser = techusers;
    }
    if (category == 'Fashion & Beauty') {
        var distSeries = fashiondistcount;
        var distuser = fashionusers;
    }    
    if (category == 'Sports & Fitness') {
        var distSeries = sportsdistcount;
        var distuser = sportsusers;
    }
    if (category == 'Arts & Culture') {
        var distSeries = artdistcount;
        var distuser = artusers;
    }
    if (category == 'Food & Drink') {
        var distSeries = fooddistcount;
        var distuser = foodusers;
    }
    if (category == 'News & Politics') {
        var distSeries = poldistcount;
        var distuser = polusers;
    }
    if (category == 'Business & Finance') {
        var distSeries = bizdistcount;
        var distuser = bizusers;
    }
    if (category == 'Unknown') {
        var distSeries = nobiodistcount;
        var distuser = nobiousers;
    }
    if (category == 'Gaming') {
        var distSeries = gamingdistcount;
        var distuser = gamingusers;
    }
    if (category == 'Music') {
        var distSeries = musicdistcount;
        var distuser = musicusers;
    }
    if (category == null) {
        var category = 'All Followers'
        var distSeries = fulldistcount;
        var distuser = fullusers;
        var text = 'Distribution of Follower Influence';
    }

        $('#dist').highcharts({
        chart: {
          type: 'spline',
          zoomType: 'x'
        },
        colors: ['#6c4096'],
        title: {
          text: text
        },
        subtitle: {
          text: 'Number of Followers at each Influence Level normal'
        },
        xAxis: {
          labels: {
            overflow: 'justify'
        },
            title: {text: 'Influence Score'}
        },
        yAxis: {
          minPadding: 30,
          title: {
            text: 'Number of Followers'
          },
          minorGridLineWidth: 0,
          gridLineWidth: 0,
          alternateGridColor: null,

        },        
        tooltip: {
          valueSuffix: ' followers'
        },
        plotOptions: {
            series: {
                allowPointSelect: true,
                point: {
                    events: {
                        click: function(event) {
                           var listUser = (distuser[this.category]);

                           console.log(listUser);
                           appendToHtmlNoBio(listUser, "#usersDisplay", "#list2");
                        }
                    }
                }
            },
          spline: {
            lineWidth: 3,
            states: {
              hover: {
                lineWidth: 4
              }
            },
            marker: {
              enabled: false
            },
    
            pointStart: 0
          }
        },
        series: [{
          name: ""+category+"",
          data: distSeries    
        }],
        navigation: {
          menuItemStyle: {
            fontSize: '10px'
          }
        }
      });
}





    
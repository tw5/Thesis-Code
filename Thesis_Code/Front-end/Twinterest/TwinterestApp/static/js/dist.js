console.log(nobiodist)

$(function() {
  $('#dist').highcharts({
    chart: {
      type: 'spline',
      zoomType: 'x'
    },
    colors: ['#6c4096'],
    title: {
      text: 'Distribution of Follower Influence'
    },
    subtitle: {
      text: 'Number of Followers at each Influence Level || Click & Drag to Zoom'
    },
    xAxis: {
      labels: {
        overflow: 'justify'
      },title: {text: 'Influence Score'}
    },
    yAxis: {
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
                          console.log(this.category);
                           var listUser = (fullusers[this.category]);

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
      name: 'Full',
      data: fulldistcount
    }],
    navigation: {
      menuItemStyle: {
        fontSize: '10px'
      }
    }
  });
});



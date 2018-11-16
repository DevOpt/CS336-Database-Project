import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BarsService, Bars, BarMenuItem, TopSpenders, TopBeers } from '../bars.service';
import { HttpResponse } from '@angular/common/http';

declare const Highcharts: any;

@Component({
  selector: 'app-bar-details',
  templateUrl: './bar-details.component.html',
  styleUrls: ['./bar-details.component.css']
})
export class BarDetailsComponent implements OnInit {

  barName: string;
  barDetails: Bars;
  menu: BarMenuItem;
  topSpenders: TopSpenders;
  topBeers: TopBeers;

  constructor(
    private barService: BarsService,
    private route: ActivatedRoute
  ) { 
    route.paramMap.subscribe((paramMap) => {
      this.barName = paramMap.get('bar');

      barService.getBar(this.barName).subscribe(
        data => {
          this.barDetails = data;
        },
        (error: HttpResponse<any>) => {
          if(error.status === 404){
            alert('Bar not found');
          }else{
            console.error(error.status + ' - ' + error.body);
            alert('An error occured on the server. Please check the console.')
          }
        }
      );

      barService.getMenu(this.barName).subscribe(
        data => {
          this.menu = data;
        }
      );

      barService.getTopSpenders(this.barName).subscribe(
        data => {
          this.topSpenders = data;
          const drinkers = [];
          const total = [];

          data.forEach(drinker => {
            drinkers.push(drinker.drinker);
            total.push(drinker.total);
          });

          this.renderSpenderChart(drinkers, total);
        }
      );

      barService.getTopBeers(this.barName).subscribe(
        data => {
          this.topBeers = data;
          const beerName = [];
          const total = [];

          data.forEach(beer => {
            beerName.push(beer.BeerName);
            total.push(beer.total);
          });

          this.renderBeerChart(beerName, total);
        }
      );
      
    });
  }

  renderSpenderChart(spenders: string[], counts: number[]) {
    Highcharts.chart('spenderbargraph', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Top 10 Spenders'
      },
      xAxis: {
        categories: spenders,
        title: {
          text: 'Drinkers'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total in $'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        bar: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: counts
      }]

    })
  }

  renderBeerChart(beer: string[], counts: number[]) {
    Highcharts.chart('beerbargraph', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Top 10 Beers Sold'
      },
      xAxis: {
        categories: beer,
        title: {
          text: 'Beer'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Sold Amount'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        bar: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: counts
      }]

    })
  }

  ngOnInit() {
  }

}

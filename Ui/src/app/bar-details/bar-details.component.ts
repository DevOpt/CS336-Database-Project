import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BarsService, Bars, BarMenuItem, TopSpenders, TopBeers, NumOfTransactions, PopularTimes } from '../bars.service';
import { HttpResponse } from '@angular/common/http';
import { SelectItem } from 'primeng/components/common/selectitem';

declare const Highcharts: any;

interface City {
  name: string;
  code: string;
}

@Component({
  selector: 'app-bar-details',
  templateUrl: './bar-details.component.html',
  styleUrls: ['./bar-details.component.css']
})
export class BarDetailsComponent implements OnInit {

  barName: string;
  barDetails: Bars;
  popularTimes: PopularTimes;
  menu: BarMenuItem;
  topSpenders: TopSpenders;
  topBeers: TopBeers;
  numOfTransactions: NumOfTransactions;
  inventoryFraction: string;

  filterDate: SelectItem[];
  filtered: SelectItem;

  cities1: SelectItem[];
  cities2: City[];
  selectedCity1: City;
  selectedCity2: City;

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

      barService.getPopularTimes(this.barName).subscribe(
        data => {
          this.popularTimes = data;
          const time = [];
          const total = [];

          data.forEach(element => {
            time.push(element.time);
            total.push(element.trans_per_hour);
          });

          this.renderPopularTimes(time, total);
        }
      )

      barService.getInventoryFraction(this.barName, 'Wednesday').subscribe(
        data => {
          this.inventoryFraction = data;
          console.log(this.selectedCity2);
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



      barService.getNumTransactions(this.barName).subscribe(
        data => {
          this.numOfTransactions = data;
          const day = [];
          const count = [];

          data.forEach(trans => {
            day.push(trans.day);
            count.push(trans.num_of_trans);
          });

          this.renderTransactionChart(day, count);
        }
      );

      this.cities1 = [
        {label:'Select City', value:null},
        {label:'New York', value:{id:1, name: 'New York', code: 'NY'}},
        {label:'Rome', value:{id:2, name: 'Rome', code: 'RM'}},
        {label:'London', value:{id:3, name: 'London', code: 'LDN'}},
        {label:'Istanbul', value:{id:4, name: 'Istanbul', code: 'IST'}},
        {label:'Paris', value:{id:5, name: 'Paris', code: 'PRS'}}
    ];

     //An array of cities
     this.cities2 = [
      {name: 'New York', code: 'NY'},
      {name: 'Rome', code: 'RM'},
      {name: 'London', code: 'LDN'},
      {name: 'Istanbul', code: 'IST'},
      {name: 'Paris', code: 'PRS'}
  ];

      this.filterDate = [
        {
          'label': 'Monday',
          'value': 'Monday'
        },
        {
          'label': 'Tuesday',
          'value': 'Tuesday'
        },
        {
          'label': 'Wednesday',
          'value': 'Wednesday'
        },
        {
          'label': 'Thursday',
          'value': 'Thursday'
        },
        {
          'label': 'Friday',
          'value': 'Friday'
        },
        {
          'label': 'Saturday',
          'value': 'Saturday'
        },
        {
          'label': 'Sunday',
          'value': 'Sunday'
        }
      ]
      
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

  renderPopularTimes(time: string[], counts: number[]) {
    Highcharts.chart('popularTimesbargraph', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Popular Times'
      },
      xAxis: {
        categories: time,
        title: {
          text: 'Time'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Customers'
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

  renderTransactionChart(day: string[], counts: number[]) {
    Highcharts.chart('transbargraph', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Number of Transactions on a given day'
      },
      xAxis: {
        categories: day,
        title: {
          text: 'Drinkers'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Transactions'
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

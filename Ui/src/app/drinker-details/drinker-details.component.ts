import { Component, OnInit } from '@angular/core';
import { DrinkersService, DrinkerTrasactions, MostOrderedBeers } from '../drinkers.service';
import { ActivatedRoute } from '@angular/router'

declare const Highcharts: any;


@Component({
  selector: 'app-drinker-details',
  templateUrl: './drinker-details.component.html',
  styleUrls: ['./drinker-details.component.css']
})
export class DrinkerDetailsComponent implements OnInit {

  drinker: string;
  drinkerTransactions: DrinkerTrasactions;
  mostOrderedBeers: MostOrderedBeers;

  constructor(
    private drinkersService: DrinkersService,
    private route: ActivatedRoute
  ) {
    route.paramMap.subscribe((paramMap) => {
      this.drinker = paramMap.get('drinker');

      this.drinkersService.getDrinkerTransactions(this.drinker).subscribe(
        data => {
          this.drinkerTransactions = data;
        }
      )

      this.drinkersService.getMostOrderedBeers(this.drinker).subscribe(
        data => {
          this.mostOrderedBeers = data;

          const beer = [];
          const ordered = [];

          data.forEach(drinker => {
            beer.push(drinker.name);
            ordered.push(drinker.beer_ordered);
          });

          this.renderMostOrderedBeers(beer, ordered);
        }
      )
    });
   }

   renderMostOrderedBeers(beer: string[], ordered: number[]) {
    Highcharts.chart('mostorderedbeers', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Most Ordered Beers'
      },
      xAxis: {
        categories: beer,
        title: {
          text: 'Beers'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Orders'
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
        data: ordered
      }]

    })
  }

  ngOnInit() {
  }

}

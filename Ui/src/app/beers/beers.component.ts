import { Component, OnInit } from '@angular/core';
import { BeersService, TopBarsFor, TopDrinkers } from '../beers.service'
import { SelectItem } from 'primeng/components/common/selectitem';

@Component({
  selector: 'app-beers',
  templateUrl: './beers.component.html',
  styleUrls: ['./beers.component.css']
})
export class BeersComponent implements OnInit {

  beers: any[];
  manufacturerOptions: SelectItem[];
  originalBeersList: any[];

  beerOptions: SelectItem[];
  originalBeerNameList: any[];

  topBars: any[];
  originalTopBars: any[];
  topBarsFor: TopBarsFor;
  topDrinkers: TopDrinkers;

  constructor(private beerService: BeersService) {
    this.beerService.getBeers().subscribe(
      data => {
        this.beers = data;
        this.originalBeersList = data;

      }
    );

    this.beerService.getBeerNames().subscribe(
      data => {
        this.beerOptions = data.map(beer => {
          return{
            label: name,
            value: name
          }
        });
      }
    );

    this.beerService.getTopBarsFor('Bass Ale').subscribe(
      data => {
        this.topBarsFor = data;
      }
    )

    this.beerService.getTopDrinkers('Bass Ale').subscribe(
      data => {
        this.topDrinkers = data;
      }
    )

    this.beerService.getBeerManufacturers().subscribe(
      data => {
        this.manufacturerOptions = data.map(manf => {
          return {
            label: manf,
            value: manf
          };
        });
      }
    );
   }

  ngOnInit() {
  }

  filterBeers(manufacturer: string){
    this.beers = this.originalBeersList;
    if(manufacturer){
      this.beers = this.originalBeersList.filter(beer => beer.manf === manufacturer);
    }
  }

  setBeer(beer: string){
    this.topBars = this.originalTopBars;
    if(beer){
      this.topBars = this.originalTopBars.filter(Select => Select.name === beer);
    }
  }

}

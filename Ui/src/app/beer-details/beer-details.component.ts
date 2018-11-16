import { Component, OnInit } from '@angular/core';
import { BeersService, BeerLocation } from '../beers.service';
import { ActivatedRoute } from '@angular/router';
import { SelectItem } from 'primeng/components/common/selectitem';


@Component({
  selector: 'app-beer-details',
  templateUrl: './beer-details.component.html',
  styleUrls: ['./beer-details.component.css']
})
export class BeerDetailsComponent implements OnInit {

  beerName: string;
  beerLocations: BeerLocation[];
  beerManf: string;

  filterOptions: SelectItem[];
  sortField: string;
  sortOrder: number;

  constructor(
    private beerService: BeersService,
    private route: ActivatedRoute
  ) { 
    route.paramMap.subscribe((paramMap) => {
      this.beerName = paramMap.get('beer');

      this.beerService.getBarSelling(this.beerName).subscribe(
        data => {
          this.beerLocations =data;
        }
      )

      this.beerService.getBeerManufacturers(this.beerName).subscribe(
        data => {
          this.beerManf = data;
        }
      );

      this.filterOptions = [
        {
          'label': 'Low price first',
          'value': 'low price'
        },
        {
          'label': 'High price first',
          'value': 'high price'
        }
      ]
    });
  }

  ngOnInit() {
  }

  sortBy(selectedOption: string){
    if(selectedOption === 'low price'){
      this.beerLocations.sort((a, b) => {
        return a.price - b.price;
      });
    } else if(selectedOption === 'high price') {
      this.beerLocations.sort((a, b) => {
        return b.price - a.price;
      });
    }
  }

}

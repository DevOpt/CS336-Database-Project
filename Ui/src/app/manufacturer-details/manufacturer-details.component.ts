import { Component, OnInit } from '@angular/core';
import { ManufacturersService, TopManfSales, CitiesLikedManf } from '../manufacturers.service';
import { ActivatedRoute } from '@angular/router';
import { SelectItem } from 'primeng/components/common/selectitem';

@Component({
  selector: 'app-manufacturer-details',
  templateUrl: './manufacturer-details.component.html',
  styleUrls: ['./manufacturer-details.component.css']
})
export class ManufacturerDetailsComponent implements OnInit {

  manf: string;
  manfSales: TopManfSales;
  citiesLikedManf: CitiesLikedManf;

  constructor(
    private manufacturersService: ManufacturersService,
    private route: ActivatedRoute
  ) { 
    route.paramMap.subscribe((paramMap) => {
      this.manf = paramMap.get('manf');

      this.manufacturersService.getTopManfSales(this.manf).subscribe(
        data => {
          this.manfSales = data;
        }
      );

      this.manufacturersService.getCitiesLikedManf(this.manf).subscribe(
        data => {
          this.citiesLikedManf = data;
        }
      )
    });
  }

  ngOnInit() {
  }

}

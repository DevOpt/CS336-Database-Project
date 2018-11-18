import { Component, OnInit } from '@angular/core';
import { DrinkersService } from '../drinkers.service';

@Component({
  selector: 'app-drinkers',
  templateUrl: './drinkers.component.html',
  styleUrls: ['./drinkers.component.css']
})
export class DrinkersComponent implements OnInit {

  drinkers: any[];

  constructor(private drinkersService: DrinkersService) {
    this.drinkersService.getDrinkers().subscribe(
      data => {
        this.drinkers = data;
      }
    )
   }

  ngOnInit() {
  }

}

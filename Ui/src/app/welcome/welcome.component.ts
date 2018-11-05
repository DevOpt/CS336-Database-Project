import { Component, OnInit } from '@angular/core';
import { BarsService, Bars } from '../bars.service';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {

  bars: Bars[];

  constructor(
    public BarService: BarsService
  ) { 
    this.getBars();
  }

  ngOnInit() {
  }

  getBars(){
    this.BarService.getBars().subscribe(
      data => {
        this.bars = data;
      },
      error => {
        alert('Could not get a list of bars.')
      }
    );
  }

}

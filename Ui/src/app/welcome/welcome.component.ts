import { Component, OnInit } from '@angular/core';
import { BarsService, Bars, TopBars } from '../bars.service';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {

  bars: Bars[];
  topBars: TopBars;
  beer: string;
  day: string;

  constructor(
    public BarService: BarsService
  ) { 
    this.getBars();

    this.BarService.getTopBars('Landshark', 'Monday').subscribe(
      data => {
        this.topBars = data;
      }
    )
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

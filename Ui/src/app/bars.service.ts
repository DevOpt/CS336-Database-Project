import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface Bars{
  name: string;
  license: string;
  city: string;
  phone: string;
  open_time: string;
  close_time: string;
}

export interface BarMenuItem{
  beer: string;
  manf: string;
  price: number;
}

export interface TopSpenders{
  drinker: string;
  total: number;
}

export interface TopBeers{
  BeerName: string;
  total: number;
}

export interface NumOfTransactions{
  day: string;
  num_of_trans: number;
}

export interface TopBars{
  bar: string;
  total_sales: number;
}

export interface PopularTimes{
  time: string;
  trans_per_hour: number;
}


@Injectable({
  providedIn: 'root'
})
export class BarsService {

  constructor(
    public http: HttpClient
  ) { }

  getBars(){
    return this.http.get<Bars[]>('/api/bar');
  }

  getBar(bar: string){
    return this.http.get<Bars>('/api/bar/' + bar);
  }

  getMenu(bar: string){
    return this.http.get<BarMenuItem>('/api/menu/' + bar);
  }

  getTopBars(beer: string, day:string){
    return this.http.get<TopBars>('/api/top-bars/' + beer +'/'+day);
  }

  getPopularTimes(bar: string){
    return this.http.get<PopularTimes>('/api/popular-times/' + bar);
  }

  getTopSpenders(bar: string){
    return this.http.get<TopSpenders>('/api/top-spenders/' + bar);
  }

  getTopBeers(bar: string){
    return this.http.get<TopBeers>('api/top-beers/' + bar);
  }

  getNumTransactions(bar: string){
    return this.http.get<NumOfTransactions>('api/transactions/' + bar);
  }

  getInventoryFraction(bar: string, day: string){
    return this.http.get<string>('api/inventory/fraction/' + bar +'/'+day);
  }
}

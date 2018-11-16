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

  getTopSpenders(bar: string){
    return this.http.get<TopSpenders>('/api/top-spenders/' + bar);
  }

  getTopBeers(bar: string){
    return this.http.get<TopBeers>('api/top-beers/' + bar)
  }
}

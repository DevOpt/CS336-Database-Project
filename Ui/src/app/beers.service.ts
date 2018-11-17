import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface BeerLocation{
  bar: string;
  price: number;
}

export interface TopBarsFor{
  bar: string;
  total_sales: number;
}

export interface TopDrinkers{
  drinker: string;
  total: number;
}

@Injectable({
  providedIn: 'root'
})
export class BeersService {

  constructor(private http: HttpClient) { }

  getBeers(){
    return this.http.get<any[]>('/api/beer')
  }

  getBeerNames(){
    return this.http.get<string>('/api/beer-name')
  }

  getBarSelling(beer: string){
    return this.http.get<BeerLocation[]>('/api/bars-selling/' + beer)
  }

  getTopBarsFor(beer: string){
    return this.http.get<TopBarsFor>('/api/top-bars/' + beer);
  }

  getTopDrinkers(beer: string){
    return this.http.get<TopDrinkers>('/api/top-drinkers/' + beer);
  }

  getBeerManufacturers(beer?: string): any{
    if(beer){
      return this.http.get<string>('/api/beer-manufacturer/' + beer);
    }
    return this.http.get<string[]>('/api/beer-manufacturer');
  }
}

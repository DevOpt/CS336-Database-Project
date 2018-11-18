import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface DrinkerTrasactions{
  ID: string;
  bar: string;
  date: string;
  items: string;
}

export interface MostOrderedBeers{
  name: string;
  beer_ordered: number;
}

@Injectable({
  providedIn: 'root'
})
export class DrinkersService {

  constructor(private http: HttpClient) { }

  getDrinkers(): any{
    return this.http.get<string>('/api/drinker')
  }

  getDrinkerTransactions(drinker: string){
    return this.http.get<DrinkerTrasactions>('/api/drinker-transactions/' + drinker);
  }

  getMostOrderedBeers(drinker: string){
    return this.http.get<MostOrderedBeers>('/api/drinker/most-ordered/' + drinker);
  }
}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface TopManfSales{
  city: string;
  city_sales: number;
}

export interface CitiesLikedManf{
  city: string;
  drinkers_like: number;
}

@Injectable({
  providedIn: 'root'
})
export class ManufacturersService {

  constructor(private http: HttpClient) { }

  getTopManfSales(manf: string){
    return this.http.get<TopManfSales>('/api/top-manf-sales/' + manf);
  }

  getCitiesLikedManf(manf: string){
    return this.http.get<CitiesLikedManf>('/api/cities-like-manf/' + manf);
  }

  getBeerManufacturers(beer?: string): any{
    if(beer){
      return this.http.get<string>('/api/beer-manufacturer/' + beer);
    }
    return this.http.get<string[]>('/api/beer-manufacturer');
  }

}

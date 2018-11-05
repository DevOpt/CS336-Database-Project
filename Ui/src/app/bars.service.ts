import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface Bars{
  name: string;
  license: string;
  city: string;
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
}

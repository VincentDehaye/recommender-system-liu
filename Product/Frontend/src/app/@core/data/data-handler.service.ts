import { Component, OnInit } from '@angular/core';
import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { Movie } from './movieClass';
import 'rxjs/add/operator/map';


@Injectable()
export class DataHandlerService {
  constructor(private http: Http) {
   }
  getData() {
    return this.http.get(`http://localhost:8000/api/v1/recommendations`)
    .map((res: Response) => res.json());
  }
}

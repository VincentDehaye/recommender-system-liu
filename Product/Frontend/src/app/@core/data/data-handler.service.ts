import { Component, OnInit } from '@angular/core';
import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { Movie } from './movieClass';
import 'rxjs/add/operator/map';


@Injectable()
export class DataHandlerService {
readonly ROOT_URL = 'http://localhost:4200/api/v1/recommendations';
  movies: Observable<Movie[]>;
  constructor(private http: HttpClient) {}
  getData(): any {
    return this.http.get(this.ROOT_URL).map((res: Response) => res);
  }
}

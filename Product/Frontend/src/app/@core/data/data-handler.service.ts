import { Component, OnInit } from '@angular/core';
import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { Movie } from './movieClass';
import 'rxjs/add/operator/map';
import { environment } from '../../../environments/environment';



@Injectable()
export class DataHandlerService {
  apiUrl: any = environment.apiUrl;
readonly ROOT_URL = this.apiUrl + '/v1/recommendations';
readonly ROOT_URLtrending = this.apiUrl + '/v1/trending';
readonly ROOT_URLyoutube = this.apiUrl + '/v1/youtubetrending';
readonly ROOT_URLtwitter = this.apiUrl + '/v1/twittertrending';
readonly ROOT_URLsimple = this.apiUrl + 'v1/simpleSuccess';
readonly ROOT_URLaverage = this.apiUrl + 'v1/averageSuccess';

  movies: Observable<Movie[]>;
  trendingMovies: Observable<Movie[]>;
  youtubeMovies: Observable<Movie[]>;
  twitterMovies: Observable<Movie[]>;
  simpleSuccess: Observable<Movie[]>;
  averageSuccess: Observable<Movie[]>;

  constructor(private http: HttpClient) {}
  getData(): any {
    return this.http.get(this.ROOT_URL).map((res: Response) => res);
  }
  getTrendingData(): any {
    return this.http.get(this.ROOT_URLtrending).map((res: Response) => res);
  }
  getYoutubeData(): any {
    return this.http.get(this.ROOT_URLyoutube).map((res: Response) => res);
  }
  getTwitterData(): any {
    return this.http.get(this.ROOT_URLtwitter).map((res: Response) => res);
  }
  getSimpleSuccessrate(): any {
    return this.http.get(this.ROOT_URLsimple).map((res: Response) => res);
  }
  getAverageSuccessrate(): any {
    return this.http.get(this.ROOT_URLaverage).map((res: Response) => res);
  }
  getMetaRecommendationsData(age_lower = 0, age_upper = 200, male = true, female = true, other = true): any {
    let filter: string = '';
    filter += 'age_lower=' + age_lower.toString() + '&age_upper=' + age_upper.toString();
    if (male) { filter += '&male=1'; }
    if (other) {filter += '&other=1'; }
    if (female) {filter += '&female=1'; }

    return this.http.get(this.ROOT_URL + '/?' + filter).map((res: Response) => res);
  }

}

import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';

@Injectable()
export class DataHandlerService {
  constructor(private http: Http) {  }
  getUser() {
    return  this.http.get('http://localhost:8000/api/v1/recommendations')
    .map((res: Response) => res.json());
  }
}

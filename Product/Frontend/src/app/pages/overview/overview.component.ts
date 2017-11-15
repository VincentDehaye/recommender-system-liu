import { Component, OnInit } from '@angular/core';

import { User } from '../authentication/_models/index';
import { UserService } from '../authentication/_services/index';
import { DataHandlerService} from '../../@core/data/data-handler.service';


@Component({
  selector: 'ngx-overview',
  styleUrls: ['./overview.component.scss'],
  templateUrl: './overview.component.html',
})
export class OverviewComponent implements OnInit {
  users: User[] = [];
  movies: string[];
  trendingMovies: string[];
  data: any;
  dataTrending: any;
  obj: any;
  // Modal headers 1-
  // Modal header for the "top recommended content"
  modalHeader1 = 'INFORMATION ABOUT THE TOP RECOMMENDED CONTENT';
  // Modal header for the "top trending content"
  modalHeader2 = 'INFORMATION ABOUT THE TOP TRENDING CONTENT';
  // Modal content 1-
  // Modal content for the "top recommended content"
  modalContent1 = `Here you can find the top recommended movies for you from our high class recommendation algorithm.`;
  // Modal content for the "top trending content"
  modalContent2 = `In this list the top trending movies are presented to you. By applicating the trending factor to the result from our recommendation algorithm, we offer you a unique experience with the most relevant movies right now. `;

    constructor(private userService: UserService, private dataHandlerService: DataHandlerService) { }

    ngOnInit() {
        // get users from secure api end point
        this.userService.getUsers()
            .subscribe(users => {
                this.users = users;
            });
        this.getData();
        this.extractData();
        this.getTrendingData();
        this.extractTrendingData();
    }
    getTrendingData() {
      this.dataHandlerService.getTrendingData().subscribe((data) => {
        this.dataTrending = data;
        // console.log(this.data); not allowed by lint ?
      });
    }
    getData() {
    this.dataHandlerService.getData().subscribe((data) => {
      this.data = data;
      // console.log(this.data); not allowed by lint ?
    }); // Converts the data making it reachable in the htm file
  }
    extractTrendingData() {
      return null;
    }
    extractData() {
    return null;
  }
}

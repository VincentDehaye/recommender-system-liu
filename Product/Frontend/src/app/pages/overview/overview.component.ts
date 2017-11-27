import { Component, OnInit } from '@angular/core';

import { User } from '../authentication/_models/index';
import { UserService } from '../authentication/_services/index';
import { DataHandlerService} from '../../@core/data/data-handler.service';


/*
  Author: Anton Bergström, Ariyan Abdulla, David Schutzer
  Date: 2017-09-30
  Last update: 2017-11-23 by Anton & Ariyan
  This contains the different components used on the overview page.
*/

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
  modalHeader1 = 'Graph for the top recommended content';
  modalHeader2 = 'List for the top recommended content';
  modalHeader3 = 'Graph for the top trending content';
  modalHeader4 = 'List for the top trending content';
  modalContent1 = `This graph shows the top recommended movies and their score produced from Coogl3's algorithm.`;
  modalContent2 = `This list shows the top recommended movies and their title.
The first movie in the list is the one with the highest score.`;
  modalContent3 = `This graph shows the top trending movies and the score produced from Coogl3's algorithm.`;
  modalContent4 = `This list shows the top trending movies and their title.
The first movie in the list is the one with the highest score.`;

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

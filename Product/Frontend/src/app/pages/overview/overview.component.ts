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
  modalHeader1 = 'Top recommended content';
  modalHeader2 = 'put description of what is shown here';
  // Modal content 1-
  modalContent1 = `this is the content that will be shown in the modal`;
  modalContent2 = `same goes for this this is for the second modal`;

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

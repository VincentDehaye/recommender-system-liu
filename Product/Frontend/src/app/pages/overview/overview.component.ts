import { Component, OnInit } from '@angular/core';

import { User } from '../authentication/_models/index';
import { UserService } from '../authentication/_services/index';


@Component({
  selector: 'ngx-overview',
  styleUrls: ['./overview.component.scss'],
  templateUrl: './overview.component.html',
})
export class OverviewComponent implements OnInit{
  users: User[] = [];

    constructor(private userService: UserService) { }

    ngOnInit() {
        // get users from secure api end point
        this.userService.getUsers()
            .subscribe(users => {
                this.users = users;
            });
    }
}

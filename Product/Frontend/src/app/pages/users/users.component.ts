import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ngx-users',
  styleUrls: ['./users.component.scss'],
  templateUrl: './users.component.html',
})

export class UsersComponent implements OnInit {
  list: any;


  ngOnInit() {
    this.list = ['Erik', 'Erik', 'Erik', 'Erik', 'Erik'];
  }
}

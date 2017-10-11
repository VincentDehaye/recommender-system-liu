import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ngx-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss'],
})
export class UserComponent implements OnInit {
  movies: string[] = ['Batman', 'Superman', 'Justice Leauge', 'The Flash', 'Wonderwoman',
   'Cyborg', 'Game of thrones', 'True detective', 'House of chaos', 'My little pony'];
  constructor() { }

  ngOnInit() {
  }
}

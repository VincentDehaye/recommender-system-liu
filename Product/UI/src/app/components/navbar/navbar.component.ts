import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  output:string ='coogbaafaopsdpasokdpl3'
  movies=[]
  constructor() { }

  ngOnInit() {
    this.output='penis'
    this.movies=['badman','watman','manman']
  }
}

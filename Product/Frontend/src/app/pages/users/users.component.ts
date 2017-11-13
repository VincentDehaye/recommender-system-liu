import { Component, OnInit } from '@angular/core';
import { DataHandlerService} from '../../@core/data/data-handler.service';


@Component({
  selector: 'ngx-users',
  styleUrls: ['./users.component.scss'],
  templateUrl: './users.component.html',
})

export class UsersComponent implements OnInit {
  movies: string[];
  data: any;


  paginationModel = 1;

  iconToolbarModel = {
    one: false,
    two: false,
  };

  constructor(private dataHandlerService: DataHandlerService) { }

  ngOnInit() {
    this.getData();
    this.extractData();


  }
  public getData(){
      this.dataHandlerService.getData().subscribe((data) => {
      this.data = data;
    }); // Converts the data making it reachable in the htm file
  }
   extractData() {
    return null;
  }
}

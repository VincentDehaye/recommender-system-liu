import { Component, OnInit } from '@angular/core';
import { DataHandlerService} from '../../@core/data/data-handler.service';
import { Observable } from 'rxjs/Observable';
import { Movie } from '../../@core/data/movieClass'
@Component({
  selector: 'ngx-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss'],
})
export class UserComponent implements OnInit {
  data: any;
  movies: string[];
  obj: any;
  constructor(private dataHandlerService: DataHandlerService) {
   }

  ngOnInit() {
    this.getData();
    // this.data = this.getData();
    // this.movies = this.data['movies'];
  }
  getData() {
    this.data = this.dataHandlerService.getData()
  }

}

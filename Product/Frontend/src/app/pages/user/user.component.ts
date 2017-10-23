import { Component, OnInit } from '@angular/core';
import { DataHandlerService} from '../../@core/data/data-handler.service';

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
    this.data = this.dataHandlerService.getData();

  }
}

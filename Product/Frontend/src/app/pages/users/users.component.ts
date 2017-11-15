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
  // Modal headers 1-
  modalHeader1 = 'This is where you decide the modal header';
  modalHeader2 = 'this is a different modal so it needs a different variable';
  modalHeader3 = 'this is a different modal so it needs a different variable';

  // Modal content 1-
  modalContent1 = `this is the content that will be shown in the modal`;
  modalContent2 = `same goes for this this is for the second modal`;
  modalContent3 = `same goes for this this is for the second modal`;

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
  public getData() {
      this.dataHandlerService.getData().subscribe((data) => {
      this.data = data;
    }); // Converts the data making it reachable in the htm file
  }
   extractData() {
    return null;
  }
}

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
  modalHeader1 = 'Information about times recommended';
  modalHeader2 = 'this is a different modal so it needs a different variable';
  modalHeader3 = 'How to configure demographics';

  // Modal content 1-
  modalContent1 = `Each bar shows the number of times a certain movie has been
                    recommended and shows the top recommendations
                    depending on the demographics setting.`;
  modalContent2 = `shows a list of the top recommended movies recommended by the algorithm.`;
  modalContent3 = `explains the controlls and how they work`;

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

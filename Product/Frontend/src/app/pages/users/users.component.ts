import { Component, OnInit, Input } from '@angular/core';
import { DataHandlerService} from '../../@core/data/data-handler.service';


@Component({
  selector: 'ngx-users',
  styleUrls: ['./users.component.scss'],
  templateUrl: './users.component.html',
})

export class UsersComponent implements OnInit {
  model = {
    male: true,
    other: true,
    female: true,
  };
  movies: string[];
  data: any;
  value: any= '0 - 200';

  // Gender control variables initiates as true;
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

  }
  public getData() {
      this.dataHandlerService.getData().subscribe((data) => {
      this.data = data;
    }); // Converts the data making it reachable in the htm file
  }
   setAge(fromAge: any, toAge: any) {
    this.value = fromAge.toString() + ' - ' + toAge.toString();
  }
   enableGender() {
     return null;
   }
}

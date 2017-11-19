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
  modalHeader1 = 'Graph displaying the number of times a movie has been recommended';
  modalHeader2 = 'List for the top recommended content';
  modalHeader3 = 'Demographic settings';

  // Modal content 1-
  modalContent1 = `Each bar shows the number of times a certain movie has been
                    recommended and shows the top recommendations
                    depending on the demographics setting.`;
  modalContent2 = `This list shows the top recommended movies and their title. 
  The first movie in the list is the one with the highest score.`;
  modalContent3 = `Default setting: all users in the database are taken into consideration.
 Use the numbered buttons to change the age interval.
 Use the gender buttons to change the gender demographic.`;

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

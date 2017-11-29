// Performance page
import { Component, OnInit } from '@angular/core';
import { DataHandlerService} from '../../@core/data/data-handler.service';

/*
  Author: Anton Bergström, Ariyan Abdulla, David Schutzer
  Date: 2017-09-30
  Last update: 2017-11-23 by Anton & Ariyan
  This contains the different components used on the performance page.
*/

@Component({
  selector: 'ngx-recommended',
  styleUrls: ['./recommended.component.scss'],
  templateUrl: './recommended.component.html',
})
export class RecommendedComponent implements OnInit {
  simpleSuccessrate: string[];
  averageSuccessrate: string[];
  dataSimple: any;
  dataAverage: any;
  modalHeader1 = 'Graph that displays the improvement over time for the Coogl3 algorithm.';
  modalContent1 = `Each dot on the graph is connected to a certain time and success rate
  for the algorithm. The success rate is
based on the end-users reaction to watching content
from movies that have been recommended for them.`;

  constructor(private dataHandlerService: DataHandlerService) { }
  ngOnInit() {
    this.getSimpleSuccessrate();
    this.getAverageSuccessrate();
  }
   getSimpleSuccessrate() {
      this.dataHandlerService.getSimpleSuccessrate().subscribe((data) => {
        this.dataSimple = data;
        // console.log(this.data); not allowed by lint ?
      });
    }
     getAverageSuccessrate() {
      this.dataHandlerService.getAverageSuccessrate().subscribe((data) => {
        this.dataAverage = data;
        // console.log(this.data); not allowed by lint ?
      });
    }
    extractAvergaeSuccessrate() {
      return null;
    }
    extractSimpleSuccessrate() {
    return null;
  }

}

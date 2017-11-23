// Performance page
import { Component, OnInit } from '@angular/core';
import { DataHandlerService} from '../../@core/data/data-handler.service';

@Component({
  selector: 'ngx-recommended',
  styleUrls: ['./recommended.component.scss'],
  templateUrl: './recommended.component.html',
})
export class RecommendedComponent implements OnInit{
  simpleSuccessrate: string[];
  averageSuccessrate: string[];
  dataSimple: any;
  dataAverage: any;
  modalHeader1 = 'Graph that displays the improvement over time for the Coogl3 algorithm.';
  // Modal content 1-
  modalContent1 = `Each dot on the graph is connected to a certain time and success rate
  for the algorithm. The success rate is
based on the end-users reaction to watching content,
this is determined by whether they liked or disliked a movie from the generated
recommendations list.`;

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

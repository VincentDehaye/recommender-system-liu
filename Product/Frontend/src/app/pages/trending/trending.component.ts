import { Component, OnInit } from '@angular/core';

import { DataHandlerService} from '../../@core/data/data-handler.service';

@Component({
  selector: 'ngx-trending',
  styleUrls: ['./trending.component.scss'],
  templateUrl: './trending.component.html',
})
export class TrendingComponent implements OnInit {
  trendingMovies: string[];
  youtubeMovies: string[];
  twitterMovies: string[];
  dataTrending: any;
  dataYoutube: any;
  dataTwitter: any;
  // Modal headers 1-
  modalHeader1 = 'This is where you decide the modal header';
  modalHeader2 = 'this is a different modal so it needs a different variable';
  modalHeader3 = 'this is a different modal so it needs a different variable';

  // Modal content 1-
  modalContent1 = `this is the content that will be shown in the modal`;
  modalContent2 = `same goes for this this is for the second modal`;
  modalContent3 = `same goes for this this is for the second modal`;


    constructor(private dataHandlerService: DataHandlerService) { }

    ngOnInit() {
        this.getTrendingData();
        this.extractTrendingData();
        this.getYoutubeData();
        this.extractYoutubeData();
        this.getTwitterData();
        this.extractTwitterData();

    }
    getTrendingData() {
      this.dataHandlerService.getTrendingData().subscribe((data) => {
        this.dataTrending = data;
        // console.log(this.data); not allowed by lint ?
      });
    }
    getYoutubeData() {
    this.dataHandlerService.getYoutubeData().subscribe((data) => {
      this.dataYoutube = data;
      // console.log(this.data); not allowed by lint ?
    }); // Converts the data making it reachable in the htm file
  }
  getTwitterData() {
    this.dataHandlerService.getTwitterData().subscribe((data) => {
      this.dataTwitter = data;
      // console.log(this.data); not allowed by lint ?
    }); // Converts the data making it reachable in the htm file
  }
    extractTrendingData() {
      return null;
    }
    extractYoutubeData() {
    return null;
  }
   extractTwitterData() {
    return null;
  }
}

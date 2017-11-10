import { Component, OnInit } from '@angular/core';

import { DataHandlerService} from '../../@core/data/data-handler.service';

@Component({
  selector: 'ngx-trending',
  styleUrls: ['./trending.component.scss'],
  templateUrl: './trending.component.html',
})
export class TrendingComponent implements OnInit{
  trendingMovies: string[];
  youtubeMovies: string[];
  twitterMovies: string[];
  dataTrending: any;
  dataYoutube: any;
  dataTwitter: any;

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


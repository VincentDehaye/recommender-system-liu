import { Component, OnDestroy, OnInit, Input } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { TrendingComponent } from '../trending.component'
import { DataHandlerService} from '../../../@core/data/data-handler.service';


@Component({
  selector: 'ngx-d3-bar',
  template: `
    <ngx-charts-bar-vertical
      [scheme]="colorScheme"
      [results]="results"
      [xAxis]="showXAxis"
      [yAxis]="showYAxis"
      [legend]="showLegend"
      [xAxisLabel]="xAxisLabel"
      [yAxisLabel]="yAxisLabel">
    </ngx-charts-bar-vertical>
  `,
})
export class TrendingD3BarComponent implements OnDestroy, OnInit {
  @Input() factor: number;
  movies: string[];
  data: any;
  results = [];
  showLegend = false;
  showXAxis = true;
  showYAxis = true;
  xAxisLabel = 'Title';
  yAxisLabel = 'Score';
  colorScheme: any;
  themeSubscription: any;

  constructor(private theme: NbThemeService, private dataHandlerService: DataHandlerService) {
    this.themeSubscription = this.theme.getJsTheme().subscribe(config => {
      const colors: any = config.variables;
      this.colorScheme = {
        domain: [colors.primaryLight, colors.infoLight, colors.successLight, colors.warningLight, colors.dangerLight],
      };
    });
  }

  ngOnInit() {
    this.getData();
    this.extractData();



  }
  public getData() {
      if (this.factor == 1){
        this.dataHandlerService.getTrendingData().subscribe((data) => {
      this.movies = data.trendingMovies;

      this.results = [
        { name: this.movies[0]['title'], value: this.movies[0]['score']},
        { name: this.movies[1]['title'], value: this.movies[1]['score']},
        { name: this.movies[2]['title'], value: this.movies[2]['score']},
        { name: this.movies[3]['title'], value: this.movies[3]['score']},
        { name: this.movies[4]['title'], value: this.movies[4]['score']},
        { name: this.movies[5]['title'], value: this.movies[5]['score']},
        { name: this.movies[6]['title'], value: this.movies[6]['score']},
        { name: this.movies[7]['title'], value: this.movies[7]['score']},
        { name: this.movies[8]['title'], value: this.movies[8]['score']},
        { name: this.movies[9]['title'], value: this.movies[9]['score']},
        ]
    });

      }
      if (this.factor == 2){
        this.dataHandlerService.getYoutubeData().subscribe((data) => {
      this.movies = data.youtubeMovies;

      this.results = [
        { name: this.movies[0]['title'], value: this.movies[0]['score']},
        { name: this.movies[1]['title'], value: this.movies[1]['score']},
        { name: this.movies[2]['title'], value: this.movies[2]['score']},
        { name: this.movies[3]['title'], value: this.movies[3]['score']},
        { name: this.movies[4]['title'], value: this.movies[4]['score']},
        { name: this.movies[5]['title'], value: this.movies[5]['score']},
        { name: this.movies[6]['title'], value: this.movies[6]['score']},
        { name: this.movies[7]['title'], value: this.movies[7]['score']},
        { name: this.movies[8]['title'], value: this.movies[8]['score']},
        { name: this.movies[9]['title'], value: this.movies[9]['score']},
        ]
    });

      }
      if (this.factor == 3){
        this.dataHandlerService.getTwitterData().subscribe((data) => {
      this.movies = data.twitterMovies;

      this.results = [
        { name: this.movies[0]['title'], value: this.movies[0]['score']},
        { name: this.movies[1]['title'], value: this.movies[1]['score']},
        { name: this.movies[2]['title'], value: this.movies[2]['score']},
        { name: this.movies[3]['title'], value: this.movies[3]['score']},
        { name: this.movies[4]['title'], value: this.movies[4]['score']},
        { name: this.movies[5]['title'], value: this.movies[5]['score']},
        { name: this.movies[6]['title'], value: this.movies[6]['score']},
        { name: this.movies[7]['title'], value: this.movies[7]['score']},
        { name: this.movies[8]['title'], value: this.movies[8]['score']},
        { name: this.movies[9]['title'], value: this.movies[9]['score']},
        ]
    });

      }
      // Converts the data making it reachable in the htm file
  }
   extractData() {
    return null;
  }


  ngOnDestroy(): void {
    this.themeSubscription.unsubscribe();
  }
}

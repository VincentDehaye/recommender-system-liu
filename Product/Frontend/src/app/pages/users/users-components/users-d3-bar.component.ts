import { Component, OnDestroy, OnInit } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { UsersComponent } from '../users.component'
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
export class UsersD3BarComponent implements OnDestroy, OnInit {

  movies: string[];
  data: any;
  results = [];
  showLegend = false;
  showXAxis = true;
  showYAxis = true;
  xAxisLabel = 'movies';
  yAxisLabel = 'recomended';
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
      this.dataHandlerService.getData().subscribe((data) => {
      this.movies = data.recommendation_list;
      // console.log();
        // console.log(this.movies[0]["name"]);
       // console.log(this.movies.values());
     /* var i:number;
      for (i = 0;i < 9; ++i){
        this.results.push({name: this.movies[1]["name"], value: this.movies[1]['id']});
      }*/
      this.results = [
        { name: this.movies[0]['title'], value: this.movies[0]['timesRecommended']},
        { name: this.movies[1]['title'], value: this.movies[1]['timesRecommended']},
        { name: this.movies[2]['title'], value: this.movies[2]['timesRecommended']},
        { name: this.movies[3]['title'], value: this.movies[3]['timesRecommended']},
        { name: this.movies[4]['title'], value: this.movies[4]['timesRecommended']},
        { name: this.movies[5]['title'], value: this.movies[5]['timesRecommended']},
        { name: this.movies[6]['title'], value: this.movies[6]['timesRecommended']},
        { name: this.movies[7]['title'], value: this.movies[7]['timesRecommended']},
        { name: this.movies[8]['title'], value: this.movies[8]['timesRecommended']},
        { name: this.movies[9]['title'], value: this.movies[9]['timesRecommended']},
        ]
    }); // Converts the data making it reachable in the htm file
  }
   extractData() {
    return null;
  }


  ngOnDestroy(): void {
    this.themeSubscription.unsubscribe();
  }
}

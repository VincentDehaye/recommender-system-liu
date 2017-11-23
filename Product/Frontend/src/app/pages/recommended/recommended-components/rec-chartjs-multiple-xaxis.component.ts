import { Component, OnDestroy, OnInit, Input } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { DataHandlerService} from '../../../@core/data/data-handler.service';

@Component({
  selector: 'ngx-chartjs-multiple-xaxis',
  template: `
    <chart type="line" [data]="data" [options]="options"></chart>
  `,
})
export class RecommendedChartjsMultipleXaxisComponent implements OnDestroy, OnInit {
  @Input() factor: number;
  data: {};
  movies: string[];
  movies1: string[];
  options: any;
  themeSubscription: any;

  constructor(private theme: NbThemeService, private dataHandlerService: DataHandlerService) {
    this.themeSubscription = this.theme.getJsTheme().subscribe(config => {

      const colors: any = config.variables;
      const chartjs: any = config.variables.chartjs;

      this.data = {
        labels: [],
        datasets: [{
          label: 'Success over time',
          data: [],
          borderColor: colors.successLight,
          backgroundColor: colors.successLight,
          fill: false,
          pointRadius: 8,
          pointHoverRadius: 10,
        }],
      };

      this.options = {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          position: 'bottom',
          labels: {
            fontColor: chartjs.textColor,
          },
        },
        hover: {
          mode: 'index',
        },
        scales: {
          xAxes: [
            {
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Month',
              },
              gridLines: {
                display: true,
                color: chartjs.axisLineColor,
              },
              ticks: {
                fontColor: chartjs.textColor,
              },
            },
          ],
          yAxes: [
            {
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Value(%)',
              },
              gridLines: {
                display: true,
                color: chartjs.axisLineColor,
              },
              ticks: {
                fontColor: chartjs.textColor,
              },
            },
          ],
        },
      };
    });
  }

  ngOnInit() {
    this.getData();
    this.extractData();
  }
  getData() {




    if (this.factor === 1) {
      this.dataHandlerService.getAverageSuccessrate().subscribe((data) => {
        this.movies1 = data.averageSuccess;
        this.dataHandlerService.getSimpleSuccessrate().subscribe((data) => {
          this.movies = data.simpleSuccess;

          this.data = {
            labels: [this.movies[0]['time'], this.movies[1]['time'], this.movies[2]['time'],
              this.movies[3]['time'], this.movies[4]['time'], this.movies[5]['time']],
            datasets: [{
              label: 'Success over time simple',
              data: [this.movies[0]['rate'], this.movies[1]['rate'], this.movies[2]['rate'],
                this.movies[3]['rate'], this.movies[4]['rate'], this.movies[5]['rate']],
              borderColor: '#FF3DD6',
              backgroundColor: '#ffffff',
              fill: false,
              pointRadius: 8,
              pointHoverRadius: 10,
            }, {
              label: 'Success over time average',
              data: [this.movies1[0]['rate'], this.movies1[1]['rate'], this.movies1[2]['rate'],
                this.movies1[3]['rate'], this.movies1[4]['rate'], this.movies1[5]['rate']],
              borderColor: '#31ff1e',
              backgroundColor: '#ffffff',
              fill: false,
              pointRadius: 8,
              pointHoverRadius: 10,
            }],
          }
        });
      });
    }

  }
  extractData() {
    return null;
  }

  ngOnDestroy(): void {
    this.themeSubscription.unsubscribe();
  }

  private random() {
    return Math.round(Math.random() * 100);
  }
}

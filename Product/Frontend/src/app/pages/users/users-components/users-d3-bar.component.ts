import { Component, OnDestroy } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { UsersComponent } from '../users.component'

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
export class UsersD3BarComponent implements OnDestroy {
  results = [
    { name: 'name', value: 8940 },
    { name: 'Frozen', value: 5000 },
    { name: 'The Room', value: 2000 },
    { name: 'Batman1', value: 8240 },
    { name: 'Batman2', value: 8340 },
    { name: 'Batman3', value: 8540 },
    { name: 'Batman4', value: 8640 },
    { name: 'Batman5', value: 8840 },
    { name: 'Batman6', value: 8940 },
    { name: 'Batman7', value: 8140 },
  ];
  showLegend = true;
  showXAxis = true;
  showYAxis = true;
  xAxisLabel = 'movies';
  yAxisLabel = 'recomended';
  colorScheme: any;
  themeSubscription: any;

  constructor(private theme: NbThemeService) {
    this.themeSubscription = this.theme.getJsTheme().subscribe(config => {
      const colors: any = config.variables;
      this.colorScheme = {
        domain: [colors.primaryLight, colors.infoLight, colors.successLight, colors.warningLight, colors.dangerLight],
      };
    });
  }

  ngOnDestroy(): void {
    this.themeSubscription.unsubscribe();
  }
}

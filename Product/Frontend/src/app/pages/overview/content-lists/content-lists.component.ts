import { Component } from '@angular/core';

@Component({
  selector: 'ngx-content-lists',
  styleUrls: ['./content-lists.component.scss'],
  templateUrl: './content-lists.component.html',
})
export class ContentListsComponent {

  contentList: any[] = [{
    title: 'Content #1',
    source: 'assets/images/camera1.jpg',
  }, {
    title: 'Content #2',
    source: 'assets/images/camera2.jpg',
  }, {
    title: 'Content #3',
    source: 'assets/images/camera3.jpg',
  }, {
    title: 'Content #4',
    source: 'assets/images/camera4.jpg',
  }];

  selectedContent: any = this.contentList[0];

  userMenu = [{
    title: 'Profile',
  }, {
    title: 'Log out',
  }];

  isSingleView: boolean = false;

  selectContent(camera: any) {
    this.selectedContent = camera;
    this.isSingleView = true;
  }
}

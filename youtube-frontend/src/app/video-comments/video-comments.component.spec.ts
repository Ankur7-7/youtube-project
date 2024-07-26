import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VideoCommentsComponent } from './video-comments.component';

describe('VideoCommentsComponent', () => {
  let component: VideoCommentsComponent;
  let fixture: ComponentFixture<VideoCommentsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VideoCommentsComponent]
    });
    fixture = TestBed.createComponent(VideoCommentsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

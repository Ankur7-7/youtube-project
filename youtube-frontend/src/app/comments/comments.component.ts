import { Component, Input } from '@angular/core';
import { CommentsService } from '../service/comments.service';
import { Comment } from '../comment.interface';

@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.scss']
})
export class CommentsComponent {

  search!: string;

  @Input() comment!:any;
}
